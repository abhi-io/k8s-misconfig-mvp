import { ThemeProvider, CssBaseline } from "@mui/material";
import theme from "./theme";
import AppLayout from "./layout/AppLayout";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppLayout>
        <Dashboard />
      </AppLayout>
    </ThemeProvider>
  );
}

export default App;
