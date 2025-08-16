import json

def parse_bus_info(entry):
    """Parses a single bus info string into a dictionary."""
    parts = [p.strip() for p in entry.split(",")]
    if len(parts) != 5:
        raise ValueError(f"Invalid format: {entry}")

    return {
        "BusNo": int(parts[0]),
        "Source": parts[1],
        "Destination": parts[2],
        "Time": parts[3],
        "Fare": int(parts[4])
    }

def main():
    print("=== Bus Info Formatter Tool ===")
    print("Enter bus details in format: BusNo, Source, Destination, Time, Fare")
    print("For multiple entries, separate them with a semicolon (;)")

    user_input = input("\nEnter bus info: ").strip()

    # Handle multiple entries
    entries = [e.strip() for e in user_input.split(";") if e.strip()]

    bus_list = []
    for entry in entries:
        try:
            bus_list.append(parse_bus_info(entry))
        except ValueError as e:
            print(f"⚠ Skipped entry: {e}")

    if bus_list:
        json_output = json.dumps(bus_list, indent=4)
        print("\n✅ JSON Output:")
        print(json_output)

        # Save to file
        with open("bus_info.json", "w", encoding="utf-8") as f:
            f.write(json_output)
        print("\n💾 Saved to bus_info.json")
    else:
        print("❌ No valid entries to save.")

if __name__ == "__main__":
    main()
