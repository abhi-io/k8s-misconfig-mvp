import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#7C4DFF", // Violet
    },
    background: {
      default: "#151539ff", // Matte black
      paper: "#16161D",
    },
  },
  shape: {
    borderRadius: 10,
  },
  typography: {
    fontFamily: "Inter, Roboto, sans-serif",
    h6: {
      fontWeight: 600,
    },
  },
});

export default theme;
