import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import signal
import sys
import pandas as pd


people = []
amounts = []
ratios = []

def plot(objects, values, xlabel, ylabel, title):
    df = pd.DataFrame({"Username": objects, "Messages": values})
    df_sorted = df.sort_values("Messages", ascending=False)
    plt.bar("Username", "Messages", data=df_sorted)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def handle_signal(_, __):
    plot(people, ratios, "Username", r"% of messages with 'ok'", "How much does each sleeperz member spam 'ok'?")
    plot(people, amounts, "Username", r"number of messages with 'ok'", "How much does each sleeperz member spam 'ok'?")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)

while True:
    person = input("Enter a username...")
    total_messages = input("Enter total messages...")
    messages_with_pattern = input("Enter number of messages with pattern...")
    ratio = int(messages_with_pattern)/int(total_messages)
    ratios.append(ratio * 100)
    amounts.append(int(messages_with_pattern))
    people.append(person)