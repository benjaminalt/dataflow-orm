#pragma once

#include <dataflow/Object.h> // Always
#include <dataflow/Factory.h> // Always
#include <dataflow/Member.h> // Always
#include <dataflow/Query.h> // Always
#include <memory> // Always
#include <string> // Always

namespace dataflow
{
class Order: public Object
{
public:
    typedef std::shared_ptr<Order> Ptr;

    Order(int orderID, int orderNumber, int personID)
    : orderID_("OrderID", orderID), orderNumber_("OrderNumber", orderNumber), personID_("PersonID", personID)
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

    // Accessors for members
    Member<int> orderID() const
    {
        return orderID_;
    }
    Member<int> orderNumber() const
    {
        return orderNumber_;
    }
    Member<int> personID() const
    {
        return personID_;
    }

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
private:
    Member<int> orderID_;
    Member<int> orderNumber_;
    Member<int> personID_;
};
}