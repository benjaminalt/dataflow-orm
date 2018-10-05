#include <dataflow/Person.h>
#include <dataflow/Order.h>
// #include <dataflow/PrintVisitor.h>

int main()
{
    dataflow::Person person(0, "Rogers", "Steve", 22);
    dataflow::Order order(0, 10, 0);
    // dataflow::PrintVisitor printVisitor;
    // person.accept(printVisitor);
    // order.accept(printVisitor);
    return 0;
}