#pragma once

#include <dataflow/Object.h> // Always
#include <dataflow/Factory.h> // Always
#include <dataflow/Member.h> // Always
#include <dataflow/Query.h> // Always
#include <memory> // Always
#include <string> // Always

namespace dataflow
{
namespace keys
{
namespace Order
{
const std::string OrderID = "OrderID";
const std::string OrderNumber = "OrderNumber";
const std::string PersonID = "PersonID";
}
}


class Order: public Object
{
public:
    typedef std::shared_ptr<Order> Ptr;

    Order(int orderID, int orderNumber, int personID)
    : Object({keys::Order::OrderID, keys::Order::OrderNumber, keys::Order::PersonID},
            {keys::Order::OrderID},
            {{keys::Order::OrderID, orderID}, {keys::Order::OrderNumber, orderNumber}, {keys::Order::PersonID, personID}})
    {};

    // Methods inherited from Object
    virtual std::string tableName() const
    {
        return "Order";
    }
    virtual void accept(Visitor& visitor)
    {
        visitor.visit(this);
    }

    // Also autogenerate getters for the values

    // Static methods
    static Order::Ptr fetchOne(Factory& factory, const Query& query)
    {
        std::vector<Order::Ptr> res = factory.fetchOrders(query);
        if (res.size() > 0)
        {
            return res[0];
        }
        return nullptr;
    }
    static std::vector<Order::Ptr> fetchAll(Factory& factory, const Query& query)
    {
        return factory.fetchOrders(query);
    }
};
}