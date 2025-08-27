public class SqueakyClean {
    static String clean(String identifier) {
        StringBuilder result = new StringBuilder();
        boolean convertNextToUpper = false;

        for (int i = 0; i < identifier.length(); i++) {
            char identCh = identifier.charAt(i);

            if (identCh == ' ') {
                result.append('_');
            } else if (identCh == '-') {
                convertNextToUpper = true;
            } else if (Character.isDigit(identCh)) {
                switch (identCh) {
                    case '1':
                        result.append('l'); 
                        break;
                    case '3':
                        result.append('e'); 
                        break;
                    case '4':
                        result.append('a');
                        break;
                    case '0':
                        result.append('o'); 
                        break;
                    case '7':
                        result.append('t'); 
                        break;
                    default:
                        result.append(identCh);
                        break;
                }
            } else if (Character.isLetter(identCh)) {
                if (convertNextToUpper) {
                    result.append(Character.toUpperCase(identCh));
                    convertNextToUpper = false;
                } else {
                    result.append(identCh);
                }
            }
        }

        return result.toString();
    }
}