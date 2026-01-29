import matplotlib.pyplot as plt
import random
import time

def bubble_sort_visual(arr, pause_time=0.3):
    n = len(arr)
    
    plt.ion()  # Interactive mode
    fig, ax = plt.subplots()
    
    bars = ax.bar(range(n), arr, color='blue')
    ax.set_ylim(0, max(arr) + 5)
    
    # Add text labels on top of bars
    texts = []
    for rect, val in zip(bars, arr):
        text = ax.text(rect.get_x() + rect.get_width()/2, val + 0.3, str(val),
                       ha='center', va='bottom', fontsize=10)
        texts.append(text)
    
    for i in range(n):
        for j in range(n - i - 1):
            # Highlight bars being compared
            bars[j].set_color('red')
            bars[j+1].set_color('red')
            
            plt.pause(pause_time)
            
            # Swap if necessary
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                bars[j].set_height(arr[j])
                bars[j+1].set_height(arr[j+1])
                texts[j].set_y(arr[j] + 0.3)
                texts[j].set_text(str(arr[j]))
                texts[j+1].set_y(arr[j+1] + 0.3)
                texts[j+1].set_text(str(arr[j+1]))
            
            # Reset colors
            bars[j].set_color('blue')
            bars[j+1].set_color('blue')
    
    # Final sorted bars in green
    for bar in bars:
        bar.set_color('green')
    
    plt.ioff()
    plt.show()
    
    return arr

# Generate random numbers
nums = [random.randint(1, 50) for _ in range(10)]
print("Original array:", nums)

start_time = time.time()
sorted_nums = bubble_sort_visual(nums, pause_time=0.3)
end_time = time.time()

print("Sorted array:", sorted_nums)
print(f"Time taken: {end_time - start_time:.4f} seconds")