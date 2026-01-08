import { Card, CardContent, Typography, Box, CircularProgress } from "@mui/material";

interface GaugeCardProps {
  label: string;
  value: number; // 0 - 100
}

export default function GaugeCard({ label, value }: GaugeCardProps) {
  return (
    <Card elevation={3} sx={{ width: "100%", height: "100%" }}>
      <CardContent>
        <Typography variant="subtitle2" color="text.secondary" gutterBottom>
          {label}
        </Typography>

        <Box display="flex" justifyContent="center" alignItems="center" position="relative">
          <CircularProgress
            variant="determinate"
            value={value}
            size={120}
            thickness={5}
          />
          <Box position="absolute">
            <Typography variant="h6" fontWeight="bold">
              {value}%
            </Typography>
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
}
