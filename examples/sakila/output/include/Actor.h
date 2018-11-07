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
class Actor
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
    uint16_t actorId() const
    {
        return actorId_;
    };
    void setActorId(const uint16_t& value)
    {
        actorId_ = value;
    };
    std::string firstName() const
    {
        return firstName_;
    };
    void setFirstName(const std::string& value)
    {
        firstName_ = value;
    };
    std::string lastName() const
    {
        return lastName_;
    };
    void setLastName(const std::string& value)
    {
        lastName_ = value;
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
    uint16_t actorId_;
    std::string firstName_;
    std::string lastName_;
    boost::posix_time::ptime lastUpdate_;
};
}
}
}
