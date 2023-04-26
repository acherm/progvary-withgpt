#!/usr/bin/env julia

# You can run this script using the following command:
# $ ./your_script_name.jl Hello World Beautiful Wonderful

function main()
    valid_features = Set(["Hello", "Beautiful", "Wonderful", "World"])
    selected_features = Set{String}()

    for arg in ARGS
        if arg in valid_features
            push!(selected_features, arg)
        else
            println("Invalid feature: ", arg)
            println("Valid features are: Hello, Beautiful, Wonderful, and World")
            return
        end
    end

    if isempty(selected_features)
        println("No features selected. Please select at least one feature from: Hello, Beautiful, Wonderful, and World")
        return
    end

    result = join(selected_features, " ")
    println(result)
end

main()
