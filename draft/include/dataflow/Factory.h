#pragma once

#include <vector>
#include <memory>

namespace dataflow
{
class Query;
class Person;
class Order;

class Factory
{
public:
    virtual std::vector<std::shared_ptr<Person>> fetchPersons(const Query& query) = 0;
    virtual std::vector<std::shared_ptr<Order>> fetchOrders(const Query& query) = 0;
};
}