from abc import ABC, abstractmethod


class CustomerDAOInterface(ABC):

    @abstractmethod
    def insert_into_customers_table(self, customer_obj: Customer)->Customer:
        pass

    @abstractmethod
    def delete_from_customers_table(self, customer_id: int)->bool:
        pass