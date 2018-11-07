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
class ConstVisitor
{
public:
    virtual void visit(const Actor& actor) = 0;
    virtual void visit(const Address& address) = 0;
    virtual void visit(const Category& category) = 0;
    virtual void visit(const City& city) = 0;
    virtual void visit(const Country& country) = 0;
    virtual void visit(const Customer& customer) = 0;
    virtual void visit(const Film& film) = 0;
    virtual void visit(const FilmActor& filmActor) = 0;
    virtual void visit(const FilmCategory& filmCategory) = 0;
    virtual void visit(const FilmText& filmText) = 0;
};
}
}
}
