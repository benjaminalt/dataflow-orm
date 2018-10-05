#pragma once

#include <boost/variant.hpp>

#include <string>

namespace dataflow
{
typedef boost::variant<int, double, std::string> Value;

class Member
{
public:
    Member(const std::string& field, const Value& value)
     : field_(field), value_(value) {};
    std::string field() const
    {
        return field_;
    };
    Value get() const
    {
        return value_;
    };
private:
    std::string field_;
    Value value_;
};
}