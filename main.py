from pet import Pet

def main():
    # Create your digital pet
    coco = Pet("Coco")

    # Initial status
    coco.get_status()

    # Feed, play, and rest
    coco.eat()
    coco.play()
    coco.sleep()

    # Train some tricks
    coco.train("roll over")
    coco.train("play dead")

    # Show learned tricks
    coco.show_tricks()

    # Final status
    coco.get_status()

if __name__ == "__main__":
    main()
