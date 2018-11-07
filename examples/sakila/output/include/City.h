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
class City
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
    uint16_t cityId() const
    {
        return cityId_;
    };
    void setCityId(const uint16_t& value)
    {
        cityId_ = value;
    };
    std::string city() const
    {
        return city_;
    };
    void setCity(const std::string& value)
    {
        city_ = value;
    };
    uint16_t countryId() const
    {
        return countryId_;
    };
    void setCountryId(const uint16_t& value)
    {
        countryId_ = value;
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
    uint16_t cityId_;
    std::string city_;
    uint16_t countryId_;
    boost::posix_time::ptime lastUpdate_;
};
}
}
}
