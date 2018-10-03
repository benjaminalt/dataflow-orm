#pragma once

#include <dataflow/Visitor.h>
#include <memory>
#include <string>

namespace dataflow
{
class Object
{
typedef std::shared_ptr<Object> Ptr;
public:
    virtual std::string tableName() const = 0;
    virtual void accept(Visitor& visitor) = 0;
};
}