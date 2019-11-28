/*
 * File: Collatz.cpp
 * Version: C++17
 *
 * Created by: Craig Fouts
 * Created on: 11/28/2019
 *
 * Synopsis: Runs the Collatz Conjecture for a given integer
 */

#include <iostream>

using namespace std;

// Function prototypes
int get_num(int lim);
bool is_even(int n);
void run_collatz(int n);

int main()
{
    int num(0);

    // Get number
    num = get_num(0);

    // Run Collatz Conjecture
    run_collatz(num);

    return 0;
}

// Function definitions

/**
 * Prompt for and get integer input from the user
 *
 * @param lim Lower limit for input
 * @return number given by the user
 */
int get_num(int lim)
{
    int number(0); // Number given by the user

    cout << "Please enter an integer greater than " << lim << ":";
    cin >> number;

    // Verify that number is within a valid range
    while(number <= lim)
    {
        cout << "Please enter an integer greater than " << lim << ":";
        cin >> number;
    }

    return number;
}

/**
 * Determine whether a given integer is even
 *
 * @param n Number being checked
 * @return true if n is even and false if odd
 */
bool is_even(int n)
{
    return n % 2 == 0;
}

/**
 * Run the Collatz Conjecture for a given integer
 *
 * @param n Number being run
 */
void run_collatz(int n)
{
    while (n != 1)
    {
        if (is_even(n))
        {
            n = int(n / 2);
        }
        else
        {
            n = int(n * 3 + 1);
        }
        cout << n << endl;
    }
}