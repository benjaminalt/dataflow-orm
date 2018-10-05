#pragma once

#include <dataflow/Object.h> // Always
#include <dataflow/Factory.h> // Always
#include <dataflow/Member.h> // Always
#include <dataflow/Query.h> // Always
#include <memory> // Always
#include <string> // Always

namespace dataflow
{
namespace keys
{
namespace Person
{
const std::string PersonID = "PersonID";
const std::string LastName = "LastName";
const std::string FirstName = "FirstName";
const std::string Age = "Age";
}
}

class Person: public Object
{
public:
    typedef std::shared_ptr<Person> Ptr;

    Person(int personID, const std::string& lastName, const std::string& firstName, int age)
    : Object({keys::Person::PersonID, keys::Person::LastName, keys::Person::FirstName, keys::Person::Age},
            {keys::Person::PersonID},
            {{keys::Person::PersonID, personID}, {keys::Person::LastName, lastName}, {keys::Person::FirstName, firstName}, {keys::Person::Age, age}})
    {};

    // Methods inherited from Object
    virtual std::string tableName() const
    {
        return "Person";
    }
    virtual void accept(Visitor& visitor)
    {
        visitor.visit(this);
    }

    // Also autogenerate getters for the values

    // Static methods
    static Person::Ptr fetchOne(Factory& factory, const Query& query)
    {
        std::vector<Person::Ptr> res = factory.fetchPersons(query);
        if (res.size() > 0)
        {
            return res[0];
        }
        return nullptr;
    }
    static std::vector<Person::Ptr> fetchAll(Factory& factory, const Query& query)
    {
        return factory.fetchPersons(query);
    }
};
}