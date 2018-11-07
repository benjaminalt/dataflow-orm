/**
* dataflow version 0.0.1
**/

#pragma once

#include <ConstVisitor.h>
#include <string>
#include <boost/optional.hpp>
#include <stdint.h>
#include <Visitor.h>

namespace a
{
namespace b
{
namespace c
{
class FilmText
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
    int16_t filmId() const
    {
        return filmId_;
    };
    void setFilmId(const int16_t& value)
    {
        filmId_ = value;
    };
    std::string title() const
    {
        return title_;
    };
    void setTitle(const std::string& value)
    {
        title_ = value;
    };
    boost::optional<std::string> description() const
    {
        return description_;
    };
    void setDescription(const boost::optional<std::string>& value)
    {
        description_ = value;
    };
private:
    int16_t filmId_;
    std::string title_;
    boost::optional<std::string> description_;
};
}
}
}
