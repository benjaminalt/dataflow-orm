/**
* dataflow version 0.0.1
**/

#pragma once

#include <ConstVisitor.h>
#include <stdint.h>
#include <Visitor.h>
#include <boost/date_time/posix_time/posix_time.hpp>

namespace a
{
namespace b
{
namespace c
{
class FilmActor
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
    uint16_t actorId() const
    {
        return actorId_;
    };
    void setActorId(const uint16_t& value)
    {
        actorId_ = value;
    };
    uint16_t filmId() const
    {
        return filmId_;
    };
    void setFilmId(const uint16_t& value)
    {
        filmId_ = value;
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
    uint16_t actorId_;
    uint16_t filmId_;
    boost::posix_time::ptime lastUpdate_;
};
}
}
}
