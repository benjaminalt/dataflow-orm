#pragma once

#include <string>

namespace dataflow
{
class Factory;

template <typename ValueType>
class Member
{
public:
    Member(const std::string& field, const ValueType& value)
     : field_(field), value_(value) {};
    std::string field() const
    {
        return field_;
    };
    ValueType get() const
    {
        return value_;
    };
private:
    std::string field_;
    ValueType value_;
};
}