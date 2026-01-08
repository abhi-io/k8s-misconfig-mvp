import { Card, CardContent, Typography, Box } from "@mui/material";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";

interface MetricCardProps {
  title: string;
  value: string;
  subtitle?: string;
  icon?: React.ReactNode;
}

export default function MetricCard({
  title,
  value,
  subtitle,
  icon = <TrendingUpIcon />,
}: MetricCardProps) {
  return (
    <Card elevation={3} sx={{ width: "100%", height: "100%" }}>
      <CardContent>
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Box>
            <Typography variant="subtitle2" color="text.secondary">
              {title}
            </Typography>
            <Typography variant="h4" fontWeight="bold">
              {value}
            </Typography>
            {subtitle && (
              <Typography variant="caption" color="text.secondary">
                {subtitle}
              </Typography>
            )}
          </Box>
          <Box fontSize={40} color="primary.main">
            {icon}
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
}
