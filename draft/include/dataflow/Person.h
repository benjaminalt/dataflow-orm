#pragma once

#include <dataflow/Object.h> // Always
#include <dataflow/Factory.h> // Always
#include <dataflow/Member.h> // Always
#include <dataflow/Query.h> // Always
#include <memory> // Always
#include <string> // Always

namespace dataflow
{
class Person: public Object
{
public:
    typedef std::shared_ptr<Person> Ptr;

    Person(int personID, const std::string& lastName, const std::string& firstName, int age)
    : personID_("PersonID", personID), lastName_("LastName", lastName), firstName_("FirstName", firstName), age_("Age", age)
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

    // Accessors for members
    Member<int> personID() const
    {
        return personID_;
    }
    Member<std::string> lastName() const
    {
        return lastName_;
    }
    Member<std::string> firstName() const
    {
        return firstName_;
    }
    Member<int> age() const
    {
        return age_;
    }

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
private:
    Member<int> personID_;
    Member<std::string> lastName_;
    Member<std::string> firstName_;
    Member<int> age_;
};
}