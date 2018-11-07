/**
* dataflow version 0.0.1
**/

#pragma once

#include <ConstVisitor.h>
#include <Visitor.h>
#include <string>
#include <stdint.h>
#include <boost/date_time/posix_time/posix_time.hpp>

namespace a
{
namespace b
{
namespace c
{
class Category
{
public:
    void accept(Visitor& visitor)
    {
        visitor.visit(*this);
    };
    void accept(ConstVisitor& visitor) const
    {
        visitor.visit(*this);
    };
    uint8_t categoryId() const
    {
        return categoryId_;
    };
    void setCategoryId(const uint8_t& value)
    {
        categoryId_ = value;
    };
    std::string name() const
    {
        return name_;
    };
    void setName(const std::string& value)
    {
        name_ = value;
    };
    boost::posix_time::ptime lastUpdate() const
    {
        return lastUpdate_;
    };
    void setLastUpdate(const boost::posix_time::ptime& value)
    {
        lastUpdate_ = value;
    };
private:
    uint8_t categoryId_;
    std::string name_;
    boost::posix_time::ptime lastUpdate_;
};
}
}
}
