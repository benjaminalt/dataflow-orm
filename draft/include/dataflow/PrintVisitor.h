#pragma once

#include <dataflow/Visitor.h>
#include <dataflow/Person.h>
#include <dataflow/Order.h>
#include <iostream>

namespace dataflow
{
class PrintVisitor : public Visitor
{
public:
    PrintVisitor() : indentationLevel_(0) {};
    virtual void visit(Person* person)
    {
        printTableName(person->tableName());
        printField(person->personID().field(), std::to_string(person->personID().get()));
        printField(person->firstName().field(), person->firstName().get());
        printField(person->lastName().field(), person->lastName().get());
        printField(person->age().field(), std::to_string(person->age().get()));
    }
    virtual void visit(Order* order)
    {
        printTableName(order->tableName());
        printField(order->orderID().field(), std::to_string(order->orderID().get()));
        printField(order->personID().field(), std::to_string(order->personID().get()));
        printField(order->orderNumber().field(), std::to_string(order->orderNumber().get()));
    }
private:
    void printTableName(const std::string& line) const
    {
        std::cout << std::string(indentationLevel_ * 2, ' ') << line << std::endl;
    }
    void printField(const std::string& fieldName, const std::string& value) const
    {
        std::cout << std::string(indentationLevel_ * 2, ' ') << " - " << fieldName << ": " << value << std::endl;
    }
    int indentationLevel_;
};
}