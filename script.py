import torch
import math

def encode(angle_targets):
    """Circular Smooth Label Encoder.

    Args:
        angle_targets (Tensor): Angle offset for each scale level
            Has shape (num_anchors * H * W, 1)

    Returns:
        Tensor: The csl encoding of angle offset for each scale
        level. Has shape (num_anchors * H * W, encode_size)
    """

    # radius to degree
    angle_targets_deg = angle_targets * (180 / math.pi)
    # empty label (num_anchors * H * W, encode_size)
    smooth_label = torch.zeros_like(angle_targets).repeat(
        1, 180)
    angle_targets_deg = (angle_targets_deg +
                         90)
    # Float to Int
    angle_targets_long = angle_targets_deg.long()

    # if self.window == 'pulse':
    #     radius_range = angle_targets_long % self.encode_size
    #     smooth_value = 1.0
    # elif self.window == 'rect':
    #     base_radius_range = torch.arange(
    #         -self.radius, self.radius, device=angle_targets_long.device)
    #     radius_range = (base_radius_range +
    #                     angle_targets_long) % self.encode_size
    #     smooth_value = 1.0
    # elif self.window == 'triangle':
    #     base_radius_range = torch.arange(
    #         -self.radius, self.radius, device=angle_targets_long.device)
    #     radius_range = (base_radius_range +
    #                     angle_targets_long) % self.encode_size
    #     smooth_value = 1.0 - torch.abs(
    #         (1 / self.radius) * base_radius_range)

    base_radius_range = torch.arange(
        -6 // 2,
        6 // 2,
        device=angle_targets_long.device)

    radius_range = (base_radius_range +
                    angle_targets_long) % 180
    smooth_value = torch.exp(-torch.pow(base_radius_range.float(), 2.)
                             ) / (2 * 3 ** 2)
    if isinstance(smooth_value, torch.Tensor):
        smooth_value = smooth_value.unsqueeze(0).repeat(
            smooth_label.size(0), 1)

    return smooth_label.scatter(1, radius_range, smooth_value)

x1 = torch.rand(2,1)
x1[:,0]=3
x2 = encode(x1)
print(x2)
print((2 * 6 ** 2))