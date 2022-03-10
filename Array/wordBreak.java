public static List<String> wordBreak(String s, HashSet<string> dictionary) {
    if (s == null || s.isEmpty())
        return null;

    State[] memo = new State[s.length()];
    Arrays.fill(memo, State.UNVISITED);

    List<String> result = new ArrayList<String>();

    if (wordBreak(s, 0, memo, result, dictionary)) {
        return result;
    }

    return null;
}

public static boolean wordBreak(String s, int start, state[] memo,
        List<String> result, HashSet<String> sictionary) {
    if (start == s.length())
        return true;

    if (memo[start] == State.NOT_FOUND)
        return false;

    for (int i = start; i < s.length(); i++) {
        String candidate = s.substring(start, i + 1);

        if (dictionary.contains(candidate)) {
            result.add(candidate);
            if (wordBreak(s, i + 1, memo, result, dictionary)) {
                return true;
            } else {
                result.remove(result.size() - 1); // remove candidate
                memo[i+1] = State.NOT_FOUND;
            }
        }
    }

    return false;
}

// Helper code
public emun State {
    UNVISITED;
    NOT_FOUND;
}
