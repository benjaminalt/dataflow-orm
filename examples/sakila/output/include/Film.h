/**
* dataflow version 0.0.1
**/

#pragma once

#include <stdint.h>
#include <set>
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
class Film
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
    uint16_t filmId() const
    {
        return filmId_;
    };
    void setFilmId(const uint16_t& value)
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
    boost::optional<uint16_t> releaseYear() const
    {
        return releaseYear_;
    };
    void setReleaseYear(const boost::optional<uint16_t>& value)
    {
        releaseYear_ = value;
    };
    uint8_t languageId() const
    {
        return languageId_;
    };
    void setLanguageId(const uint8_t& value)
    {
        languageId_ = value;
    };
    boost::optional<uint8_t> originalLanguageId() const
    {
        return originalLanguageId_;
    };
    void setOriginalLanguageId(const boost::optional<uint8_t>& value)
    {
        originalLanguageId_ = value;
    };
    uint8_t rentalDuration() const
    {
        return rentalDuration_;
    };
    void setRentalDuration(const uint8_t& value)
    {
        rentalDuration_ = value;
    };
    double rentalRate() const
    {
        return rentalRate_;
    };
    void setRentalRate(const double& value)
    {
        rentalRate_ = value;
    };
    boost::optional<uint16_t> length() const
    {
        return length_;
    };
    void setLength(const boost::optional<uint16_t>& value)
    {
        length_ = value;
    };
    double replacementCost() const
    {
        return replacementCost_;
    };
    void setReplacementCost(const double& value)
    {
        replacementCost_ = value;
    };
    boost::optional<std::string> rating() const
    {
        return rating_;
    };
    void setRating(const boost::optional<std::string>& value)
    {
        rating_ = value;
    };
    boost::optional<std::set<std::string>> specialFeatures() const
    {
        return specialFeatures_;
    };
    void setSpecialFeatures(const boost::optional<std::set<std::string>>& value)
    {
        specialFeatures_ = value;
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
    uint16_t filmId_;
    std::string title_;
    boost::optional<std::string> description_;
    boost::optional<uint16_t> releaseYear_;
    uint8_t languageId_;
    boost::optional<uint8_t> originalLanguageId_;
    uint8_t rentalDuration_;
    double rentalRate_;
    boost::optional<uint16_t> length_;
    double replacementCost_;
    boost::optional<std::string> rating_;
    boost::optional<std::set<std::string>> specialFeatures_;
    boost::posix_time::ptime lastUpdate_;
};
}
}
}
