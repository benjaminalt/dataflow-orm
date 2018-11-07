/**
* dataflow version 0.0.1
**/

#pragma once

#include <boost/date_time/gregorian/gregorian.hpp>
#include <stdint.h>
#include <ConstVisitor.h>
#include <string>
#include <boost/optional.hpp>
#include <Visitor.h>
#include <boost/date_time/posix_time/posix_time.hpp>

namespace a
{
namespace b
{
namespace c
{
class Customer
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
    uint16_t customerId() const
    {
        return customerId_;
    };
    void setCustomerId(const uint16_t& value)
    {
        customerId_ = value;
    };
    uint8_t storeId() const
    {
        return storeId_;
    };
    void setStoreId(const uint8_t& value)
    {
        storeId_ = value;
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
    boost::optional<std::string> email() const
    {
        return email_;
    };
    void setEmail(const boost::optional<std::string>& value)
    {
        email_ = value;
    };
    uint16_t addressId() const
    {
        return addressId_;
    };
    void setAddressId(const uint16_t& value)
    {
        addressId_ = value;
    };
    bool active() const
    {
        return active_;
    };
    void setActive(const bool& value)
    {
        active_ = value;
    };
    boost::gregorian::date createDate() const
    {
        return createDate_;
    };
    void setCreateDate(const boost::gregorian::date& value)
    {
        createDate_ = value;
    };
    boost::optional<boost::posix_time::ptime> lastUpdate() const
    {
        return lastUpdate_;
    };
    void setLastUpdate(const boost::optional<boost::posix_time::ptime>& value)
    {
        lastUpdate_ = value;
    };
private:
    uint16_t customerId_;
    uint8_t storeId_;
    std::string firstName_;
    std::string lastName_;
    boost::optional<std::string> email_;
    uint16_t addressId_;
    bool active_;
    boost::gregorian::date createDate_;
    boost::optional<boost::posix_time::ptime> lastUpdate_;
};
}
}
}
