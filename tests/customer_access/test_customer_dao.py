from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer

customer_dao = CustomerDAOImp()



def test_create_customer_record_success():
    test_customer = Customer(0, "Fabulous", "Bryan")
    returned_customer = customer_dao.insert_into_customers_table(test_customer)
    assert returned_customer.customer_id != test_customer.customer_id

def test_delete_customer_record_success():
    result = customer_dao.delete_from_customers_table(-1)
    assert result
    # i need the id of a customer in the database I want to delete
    # pass that id into the delete method
    #

