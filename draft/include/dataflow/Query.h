#pragma once

#include <vector>

namespace dataflow
{
class Constraint
{
public:
    void binaryAnd(Constraint& other)
    {
        ands.push_back(other);
    }
    void binaryOr(Constraint& other)
    {

    }
private:
    std::vector<Constraint> ands;
    std::vector<Constraint> ors;
};

class UnaryConstraint
{
    enum Op
    {
        EQ,
        LT,
        GT,
        LE,
        GE
    };
};

class BinaryConstraint
{
    enum Op
    {
        BETWEEN
    };
};

class NAryConstraint
{
    enum Op
    {
        IN
    };
};

class UnaryOp
{
    enum Op
    {
        NOT
    };
};

class BinaryOp
{
    enum Op
    {
        AND,
        OR
    };
};

// class InnerJoin
// {
// private:
//     std::string tableName;
//     Query subQuery;
// };

class OrderBy
{
public:
    enum Order
    {
        ASC,
        DESC
    };
    OrderBy(const std::string& field, Order order) : field_(field), order_(order) {};
private:
    Order order_;
    std::string field_;
};

class Query
{
public:
    OrderBy orderBy() const
    {
        return orderBy_;
    }
    unsigned int limit() const
    {
        return limit_;
    }
private:
    OrderBy orderBy_;
    unsigned int limit_;
};
}