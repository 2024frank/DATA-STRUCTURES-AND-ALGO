# match.py
# This program compares protein sequences to find the closest matches.




PROTEIN = 'STTECQLKDNRAWTSLFIHTGHTECA'
MARKERS = ['TECQRKMN', 'ALFHHTTGT', 'TTECQ', 'HT', 'ZZZ', 'TTZZZRAWT']

marker_index = 0




def compare(marker_index,a):  
        count = 0
        markers = MARKERS[marker_index]

        for y in range(len(markers)):
              if PROTEIN[a+y] == markers[y]:
                    count = count+1
        return count

def best_align(markers,count):
       markers_mismatches = len(markers) - count
       return markers_mismatches
      
def  match_report(marker_index,Best_Match, position):
            print(f" Marker {MARKERS[marker_index]} has {Best_Match} error(s) at starting position {position}.")             


def main():
    for marker_index in range(len(MARKERS)):  
        move = len(PROTEIN) - len(MARKERS[marker_index])
        markers = MARKERS[marker_index]
        Best_Match = 100
        for a in range(move):
            count = compare(marker_index, a)
            markers_mismatches = best_align(markers, count)
            if markers_mismatches < Best_Match:
                Best_Match = markers_mismatches
                position = a
        match_report(marker_index, Best_Match, position)

main()

    





