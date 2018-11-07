/**
* dataflow version 0.0.1
**/

#pragma once

namespace a
{
namespace b
{
namespace c
{
class Actor;
class Address;
class Category;
class City;
class Country;
class Customer;
class Film;
class FilmActor;
class FilmCategory;
class FilmText;
class Visitor
{
public:
    virtual void visit(Actor& actor) = 0;
    virtual void visit(Address& address) = 0;
    virtual void visit(Category& category) = 0;
    virtual void visit(City& city) = 0;
    virtual void visit(Country& country) = 0;
    virtual void visit(Customer& customer) = 0;
    virtual void visit(Film& film) = 0;
    virtual void visit(FilmActor& filmActor) = 0;
    virtual void visit(FilmCategory& filmCategory) = 0;
    virtual void visit(FilmText& filmText) = 0;
};
}
}
}
