#!/bin/bash
echo "Indoor AS923"
balena deploy HELIUM-INDOOR-AS923 -e
echo "Indoor AU915"
balena deploy HELIUM-INDOOR-AU915 -e
echo "Indoor CN470"
balena deploy HELIUM-INDOOR-CN470 -e
echo "Indoor EU868"
balena deploy HELIUM-INDOOR-EU868 -e
echo "Indoor IN865"
balena deploy HELIUM-INDOOR-IN865 -e
echo "Indoor KR920"
balena deploy HELIUM-INDOOR-KR920 -e
echo "Indoor RU864"
balena deploy HELIUM-INDOOR-RU864 -e
echo "Indoor US915"
balena deploy HELIUM-INDOOR-US915 -e

echo "Outdoor AS923"
balena deploy HELIUM-OUTDOOR-AS923 -e
echo "Outdoor AU915"
balena deploy HELIUM-OUTDOOR-AU915 -e
echo "Outdoor CN470"
balena deploy HELIUM-OUTDOOR-CN470 -e
echo "Outdoor EU868"
balena deploy HELIUM-OUTDOOR-EU868 -e
echo "Outdoor IN865"
balena deploy HELIUM-OUTDOOR-IN865 -e
echo "Outdoor KR920"
balena deploy HELIUM-OUTDOOR-KR920 -e
echo "Outdoor RU864"
balena deploy HELIUM-OUTDOOR-RU864 -e
echo "Outdoor US915"
balena deploy HELIUM-OUTDOOR-US915 -e
