import { useState } from "react";
import {
  Box,
  Drawer,
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  InputBase,
  Badge,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import NotificationsIcon from "@mui/icons-material/Notifications";
import SearchIcon from "@mui/icons-material/Search";

const drawerWidth = 240;

export default function AppLayout({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = useState(true);

  return (
    <Box display="flex" minHeight="100vh">
      {/* SIDEBAR */}
      <Drawer
        variant="permanent"
        sx={{
          width: open ? drawerWidth : 72,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: open ? drawerWidth : 72,
            backgroundColor: "#0F0F14",
            borderRight: "1px solid #1F1F2B",
            transition: "width 0.3s",
          },
        }}
      >
        <Toolbar />
        <Box px={2}>
          <Typography variant="h6" color="primary">
            {open ? "My SaaS" : "MS"}
          </Typography>
        </Box>
      </Drawer>

      {/* MAIN */}
      <Box flexGrow={1}>
        {/* HEADER */}
        <AppBar
          position="sticky"
          elevation={0}
          sx={{
            backgroundColor: "#16161D",
            borderBottom: "1px solid #1F1F2B",
          }}
        >
          <Toolbar>
            <IconButton onClick={() => setOpen(!open)}>
              <MenuIcon />
            </IconButton>

            {/* SEARCH */}
            <Box
                display="flex"
                alignItems="center"
                bgcolor="#0F0F14"
                px={2}
                py={0.75}
                borderRadius={2}
                ml={2}
                flexGrow={1}
                >
                <SearchIcon fontSize="small" sx={{ color: "text.secondary" }} />
                <InputBase
                    placeholder="Search…"
                    sx={{
                    ml: 1,
                    color: "inherit",
                    width: "100%",
                    }}
                />
                </Box>


            {/* NOTIFICATIONS */}
            <IconButton sx={{ ml: "auto" }}>
              <Badge badgeContent={3} color="primary">
                <NotificationsIcon />
              </Badge>
            </IconButton>
          </Toolbar>
        </AppBar>

        {/* PAGE CONTENT */}
        <Box p={4}>{children}</Box>
      </Box>
    </Box>
  );
}
