#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    int n = floor(log10(number)) + 1;
    int arr[n] = {};
    int i = 0;
    while (number != 0)
    {
        int digit = number % 10;
        number = number / 10;
        arr[i] = digit;
        i++;
    }
    string type;
    if (n == 15 && arr[n - 1] == 3 && (arr[n - 2] == 4 || arr[n - 2] == 7))
    {
        type = "AMEX";
    }
    else if (n == 16 && arr[n - 1] == 5 && arr[n - 2] >= 1 && arr[n - 2] <= 5)
    {
        type = "MASTERCARD";
    }
    else if ((n == 13 || n == 16) && arr[n - 1] == 4)
    {
        type = "VISA";
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }
    int factor;
    int first;
    int second;
    int sum = 0;
    if (n % 2 == 0)
    {
        for (int j = n - 1; j >= 1; j -= 2)
        {
            factor = arr[j] * 2;
            if (factor > 9)
            {
                second = factor % 10;
                first = factor / 10;
                sum += first;
                sum += second;
            }
            else
            {
                sum += factor;
            }
        }
        for (int k = 0; k <= n - 1; k += 2)
        {
            sum += arr[k];
        }
        if (sum % 10 == 0)
        {
            printf("%s\n", type);
            return 0;
        }
        else
        {
            printf("INVALID\n");
            return 0;
        }
    }
    else
    {
        for (int j = n - 2; j >= 1; j -= 2)
        {
            factor = arr[j] * 2;
            if (factor > 9)
            {
                second = factor % 10;
                first = factor / 10;
                sum += first;
                sum += second;
            }
            else
            {
                sum += factor;
            }
        }
        for (int k = 0; k <= n - 1; k += 2)
        {
            sum += arr[k];
        }
        if (sum % 10 == 0)
        {
            printf("%s\n", type);
            return 0;
        }
        else
        {
            printf("INVALID\n");
            return 0;
        }
    }
}
