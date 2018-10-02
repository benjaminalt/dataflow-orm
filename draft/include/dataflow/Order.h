#pragma once

#include <dataflow/Object.h>

namespace dataflow
{
class Order: public Object
{
public:
    virtual void accept(Visitor* visitor)
    {
        visitor->visit(this);
    }
};
}