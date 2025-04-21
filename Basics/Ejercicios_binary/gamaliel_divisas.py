from typing import Final

COP_TO_MXN: Final[float] = 0.0045
AR_TO_MXN: Final[float] = 0.048
USD_TO_MXN: Final[float] = 17.50


def request_price(message: str) -> float:
    try:
        return float(input(message))
    except ValueError:
        print("Please enter a valid number.")
        return request_price(message)

def main() -> None:    
    colombian_pesos = request_price("Enter the amount in Colombian Pesos: ")
    argentinian_pesos = request_price("Enter the amount in Argentinian Pesos: ")
    dolars = request_price("Enter the amount in Dolars: ")
    
    total_mxn = (colombian_pesos * COP_TO_MXN) + (argentinian_pesos * AR_TO_MXN) + (dolars * USD_TO_MXN)
    
    print(f"The total amount in Mexican Pesos is: {total_mxn}")
    
if __name__ == "__main__":
    main()
