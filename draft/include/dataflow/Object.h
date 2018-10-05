#pragma once

#include <dataflow/Visitor.h>

#include <boost/variant.hpp>

#include <memory>
#include <vector>
#include <map>
#include <string>
#include <stdexcept>

namespace dataflow
{
typedef boost::variant<int, double, std::string> Value;

class Object
{
typedef std::shared_ptr<Object> Ptr;
public:
    virtual std::string tableName() const = 0;
    virtual void accept(Visitor& visitor) = 0;
    std::vector<std::string> keys() const
    {
        return keys_;
    }
    std::vector<std::string> primaryKeys() const
    {
        return primaryKeys_;
    }
    Value get(const std::string& key) const
    {
        std::map<std::string, Value>::const_iterator it = members_.find(key);
        if (it == members_.end())
        {
            throw std::runtime_error("Member::get: No member for key " + key);
        }
        return it->second;
    }

protected:
    Object(const std::vector<std::string>& keys, const std::vector<std::string>& primaryKeys, const std::map<std::string, Value>& members)
    : keys_(keys), primaryKeys_(primaryKeys), members_(members)
    {};
    std::vector<std::string> keys_;
    std::vector<std::string> primaryKeys_;
    std::map<std::string, Value> members_;
};
}