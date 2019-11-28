/*
 * File: Bertrand.cpp
 * Version: C++17
 *
 * Created by: Craig Fouts
 * Created on: 11/28/2019
 *
 * Synopsis: Finds all primes between a given integer n and 2n-2
 */

#include <iostream>
#include <vector>

using namespace std;

// Function prototypes
int get_num(int lim);
unsigned long long factorial(int n);
bool is_prime(int n);
vector<int> find_primes(int n);
void display_list(const vector<int>& list);

int main()
{
    int num(0); // Number given by the user

    // Get number
    num = get_num(3);

    // Display primes
    cout << "Primes between " << num << " and " << 2 * num - 2 << ":" << endl;
    display_list(find_primes(num));

    return 0;
}

// Function definitions

/**
 * Prompt for and get integer input from the user
 *
 * @param lim Lower limit for input
 * @return number given by the user
 */
int get_num(const int lim)
{
    int number(0);

    cout << "Please enter an integer greater than " << lim << ":";
    cin >> number;

    // Verify that number is within a valid range
    while (number <= lim)
    {
        cout << "Please enter an integer greater than " << lim << ": ";
        cin >> number;
    }

    return number;
}

/**
 * Compute the factorial of a given integer
 *
 * @param n Number whose factorial is being computed
 * @return factorial of n
 */
unsigned long long factorial(const int n)
{
    unsigned long long fact(1);

    for (int i = n; i > 1; --i)
    {
        fact *= i;
    }

    return fact;
}

/**
 * Determine whether a given integer is prime using Wilson's Theorem
 *
 * @param n Number whose primality is being determined
 * @return true if n is prime and false if n is composite
 */
bool is_prime(const int n)
{
    return factorial(n - 1) % n == n - 1;
}

/**
 * Find all primes between a given integer n and 2n-2
 *
 * @param n Number used to define the range of primes
 * @return list of prime numbers between n and 2n-2
 */
vector<int> find_primes(const int n)
{
    vector<int> primes;

    for (int i = n + 1; i < 2 * n - 2; ++i)
    {
        if (is_prime(i))
        {
            primes.push_back(i);
        }
    }

    return primes;
}

/**
 * Display each element in a given list on a new line
 *
 * @param list List of elements to be displayed
 */
void display_list(const vector<int>& list)
{
    for (int i : list)
    {
        cout << i << endl;
    }
}