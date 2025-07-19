from util import fetch_price, predict

def main():

    priceData = fetch_price(max=60)

    close_price = priceData['data']

    pred = predict(close_price)
    print(pred)

if __name__ == "__main__":
    print()
    print('-'*50)
    main()