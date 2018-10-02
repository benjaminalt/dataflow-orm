#pragma once

namespace dataflow
{
class Person;
class Order;

class Visitor
{
public:
    virtual void visit(Person* person) = 0;
    virtual void visit(Order* order) = 0;
};
}