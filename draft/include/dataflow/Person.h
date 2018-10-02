#pragma once

#include <dataflow/Object.h>

namespace dataflow
{
class Person: public Object
{
public:
    virtual void accept(Visitor* visitor)
    {
        visitor->visit(this);
    }
};
}