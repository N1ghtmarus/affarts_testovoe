import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.db.models import Sum
from typing import List, Dict, Any

from users.models import User
from transactions.models import Transaction
from listings.models import Lot


def get_sellers_with_customers_and_total_sales() -> List[Dict[str, Any]]:
    """
    Скрипт который формирует информацию о продавцах с перечнем покупателей,
    которые делали покупку у этого продавца с общей суммой покупок.
    """
    sellers = User.objects.filter(role='продавец')
    sellers_list = []

    for seller in sellers:
        seller_info = {
            'seller_name': seller.username,
            'customers': [],
            'total_sales': [],
            'total_sales_all_customers': 0
        }

        lots = Lot.objects.filter(seller=seller)
        transactions = Transaction.objects.filter(lot__in=lots)

        # Получение уникальных покупателей для данного продавца
        customers = transactions.values_list('buyer__username', flat=True).distinct()

        for customer in customers:
            customer_info = {
                'customer_name': customer,
                'total_sales': 0
            }

            # Получение общей суммы покупок для данного покупателя у данного продавца
            total_sales = transactions.filter(
                buyer__username=customer
                ).aggregate(
                total_sales=Sum('total_price')
                )['total_sales'] or 0

            customer_info['total_sales'] = total_sales
            seller_info['customers'].append(customer_info)

        # Получение общей суммы всех покупок для данного продавца
        total_sales_all_customers = transactions.aggregate(
            total_sales_all_customers=Sum('total_price')
            )['total_sales_all_customers'] or 0

        seller_info['total_sales_all_customers'] = total_sales_all_customers
        sellers_list.append(seller_info)

    return sellers_list


if __name__ == '__main__':
    sellers_info = get_sellers_with_customers_and_total_sales()
    for seller_info in sellers_info:
        print(f"Продавец: {seller_info['seller_name']}")
        customers = set()
        for customer_info in seller_info['customers']:
            if customer_info['customer_name'] not in customers:
                print(f" - Покупатель: {customer_info['customer_name']}")
                print(f"   Общая сумма покупок: {customer_info['total_sales']}")
                customers.add(customer_info['customer_name'])
        print(f"Общая сумма всех покупок у продавца {seller_info['seller_name']}: {seller_info['total_sales_all_customers']}")
        print()
