#![deny(missing_docs)]

//! # Moon Phase Simulator
//!
//! All the primitives required to calculate and simulate the moon phase

// Time period moon takes to start it's phase all over in days
const MOON_PHASE_TIME_PERIOD: f64 = 29.5;
// Total angle of a circle
const FULL_CIRCLE_ANGLE: f64 = 360.0;

/// The Phase of The Moon
#[derive(Debug)]
pub enum MoonPhase {
    /// The first phase of the moon with respect to it's position angle (angle 0 or 360)
    NewMoon,

    /// The second Phase of the moon with respect to it's position angle (angle 90)
    FirstQuarter,

    /// The third Phase of the moon with respect to it's position angle (angle 180)
    FullMoon,

    /// The fourth Phase of the moon with respect to it's position angle (angle 270)
    LastQuarter,

    /// The second Phase of the moon with respect to it's position angle (angle 0 < angle < 90)
    WaxingCrescent,

    /// The second Phase of the moon with respect to it's position angle (angle 90 < angle < 360)
    WaxingGibbous,

    /// The second Phase of the moon with respect to it's position angle (angle 270 < angle < 360)
    WaningCrescent,

    /// The second Phase of the moon with respect to it's position angle (angle 180 < angle < 270)
    WaningGibbous,
}

/// The position of the moon with respect to the Earth and the Sun in angles
pub struct PositionAngle {
    angle: f64,
}

impl PositionAngle {
    /// Constructs a PositionAngle with guarantee that the resulting angle
    /// will be 0 <= angle <= 360 for whatever angle provided
    fn new(mut angle: f64) -> Self {
        if angle > FULL_CIRCLE_ANGLE {
            angle %= FULL_CIRCLE_ANGLE;
        }
        Self { angle }
    }

    /// Returns the internal angle value
    fn get_angle(&self) -> f64 {
        self.angle
    }
}

/// The Moon
pub struct Moon {
    position_angle: PositionAngle,
}

impl Moon {
    /// Creates the Moon from the provided position angle
    pub fn from_position_angle(position_angle: PositionAngle) -> Self {
        Self { position_angle }
    }

    /// Creates the moon from the days after the new moon phase
    pub fn from_days_after_new_moon(days: f64) -> Self {
        let angle = (FULL_CIRCLE_ANGLE / MOON_PHASE_TIME_PERIOD) * days;
        Self {
            position_angle: PositionAngle::new(angle),
        }
    }

    /// Gets the phase of the moon at it's current position angle
    pub fn get_phase(&self) -> MoonPhase {
        match self.position_angle.get_angle() {
            angle if angle == 0.0 || angle == 360.0 => MoonPhase::NewMoon,
            angle if angle == 90.0 => MoonPhase::FirstQuarter,
            angle if angle == 180.0 => MoonPhase::FullMoon,
            angle if angle == 270.0 => MoonPhase::LastQuarter,
            angle if 0.0 < angle && angle < 90.0 => MoonPhase::WaxingCrescent,
            angle if 90.0 < angle && angle < 180.0 => MoonPhase::WaxingGibbous,
            angle if 180.0 < angle && angle < 270.0 => MoonPhase::WaningGibbous,
            angle if 270.0 < angle && angle < 360.0 => MoonPhase::WaningCrescent,
            angle => unreachable!(
                "All the moon phases should be covered with all possible position angles, {}",
                angle
            ),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn unreachable_get_phase_test() {
        for angle in 0..360 {
            let moon = Moon::from_position_angle(PositionAngle::new(angle as f64));
            moon.get_phase();
        }
    }
}
