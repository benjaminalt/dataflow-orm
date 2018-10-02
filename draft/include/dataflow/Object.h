#pragma once

#include <dataflow/Visitor.h>

namespace dataflow
{
class Object
{
public:
    virtual void accept(Visitor* visitor) = 0;
};
}