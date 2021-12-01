import Statistics

# Read in file
depths = zeros(Int64, 0)
open("../data/input_1.txt") do file
    s = read(file, String)
    append!(depths, parse.(Int, split(s, r"\n|\r\n")))
end

# PART 1
depth_inc_counter = 0
for i in zip(depths[1:end-1],depths[2:end])
    if i[2] > i[1]
        global depth_inc_counter += 1
    end
end
println("Answer to part 1 is: ", depth_inc_counter)

# PART 2
windows = collect(zip(depths[1:end-2], depths[2:end-1], depths[3:end]))
depth_window_tuples = zip(windows[1:end-1], windows[2:end])

depth_inc_counter = 0    
for i in depth_window_tuples
    if Statistics.mean(i[2]) > Statistics.mean(i[1])
        global depth_inc_counter += 1
    end
end

println("Answer to part 2 is: ", depth_inc_counter)