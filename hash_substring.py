def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    let = input()[0]
    if let == 'F' :
        inp = input()
        if 'a' in inp:
            return
        inp = "tests/" + inp
        with open(inp) as file: 
            temp = file.read().splitlines() 
            fd = temp[0]
            text = temp[1]
    elif let == 'I' :
        fd = input()
        text = input() 

    else: 
        return
    return (fd, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    hmap = []
    nums = []
    def find_letter(let):
        for j in range(len(hmap)):
            if (let == hmap[j][0]):
                return hmap[j][1]
        return(-1)
        
    n = len(pattern)
    l = len(text)

    num = 0
    for i in range(n):
        num *= 10
        t = find_letter(text[i])
        if(t!=-1):
            num+=t
        else:
            hmap.append([text[i],len(hmap)+1])
            num+=len(hmap)
    nums.append(num)


    for i in range(n, l):

        t=find_letter(text[i-n])
        num -= (10**(n-1))*t
        num *= 10
        t=find_letter(text[i])
        if(t!=-1):
            num+=t
        else:
            hmap.append([text[i],len(hmap)+1])
            num+=len(hmap)
        nums.append(num)

    num = 0
    for i in range(n):
        num *= 10
        t = find_letter(pattern[i])
        if(t!=-1):
            num+=t
        else:
            return[-1]
    print(num)
    
    ans = []
    for i in range(len(nums)):
        if num == nums[i]:
            ans.append(i)



    return [ans]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
