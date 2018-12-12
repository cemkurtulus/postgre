from domain.Customer import Customer
from domain.CustomerBook import CustomerBook
from Repository import Repository

customerRepository = Repository(Customer)

customerBookRepository = Repository(CustomerBook)

result = customerRepository.get_all()
print(result)

for item in result:
    print(f"{item.id}-{item.name}")

result_join = customerRepository.get_all(Customer.books)

for item in result_join:
    print(f"{item.id}-{item.name}")

    for book_item in item.books:
        print(f"---{book_item.id}-{book_item.name}")

filter_result = customerRepository.filter(Customer.name == 'cem')
print(filter_result)
for filter_item in filter_result:
    print(f"{filter_item.id}-{filter_item.name}")

relation_list = customerBookRepository.get_all()

for relation_item in relation_list:
    print(relation_item.customer)
    print(f"{relation_item.id}-{relation_item.name}")
