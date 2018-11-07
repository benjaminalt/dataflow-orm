/**
* dataflow version 0.0.1
**/

#pragma once

#include <ConstVisitor.h>
#include <Visitor.h>
#include <string>
#include <boost/optional.hpp>
#include <stdint.h>
#include <boost/date_time/posix_time/posix_time.hpp>

namespace a
{
namespace b
{
namespace c
{
class Address
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
    uint16_t addressId() const
    {
        return addressId_;
    };
    void setAddressId(const uint16_t& value)
    {
        addressId_ = value;
    };
    std::string address() const
    {
        return address_;
    };
    void setAddress(const std::string& value)
    {
        address_ = value;
    };
    boost::optional<std::string> address2() const
    {
        return address2_;
    };
    void setAddress2(const boost::optional<std::string>& value)
    {
        address2_ = value;
    };
    std::string district() const
    {
        return district_;
    };
    void setDistrict(const std::string& value)
    {
        district_ = value;
    };
    uint16_t cityId() const
    {
        return cityId_;
    };
    void setCityId(const uint16_t& value)
    {
        cityId_ = value;
    };
    boost::optional<std::string> postalCode() const
    {
        return postalCode_;
    };
    void setPostalCode(const boost::optional<std::string>& value)
    {
        postalCode_ = value;
    };
    std::string phone() const
    {
        return phone_;
    };
    void setPhone(const std::string& value)
    {
        phone_ = value;
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
    uint16_t addressId_;
    std::string address_;
    boost::optional<std::string> address2_;
    std::string district_;
    uint16_t cityId_;
    boost::optional<std::string> postalCode_;
    std::string phone_;
    boost::posix_time::ptime lastUpdate_;
};
}
}
}
